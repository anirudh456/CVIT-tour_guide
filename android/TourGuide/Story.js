import React, { Component } from 'react';
import {
  Platform,
  StyleSheet,
  Text,
  View,
  Button
} from 'react-native';


import EventEmitter2 from 'eventemitter2'
window.EventEmitter2 = EventEmitter2.EventEmitter2
var RosClient = require("roslibjs-client");
var client = new RosClient({
  url: "ws://10.2.131.218:9090"
});


export default class Story extends React.Component{
  constructor(props) {
    super(props);
    this.state={
      labStory : '',
      labName: '',
      next_location_id: this.props.location_id,
      curent_location_id: '',
    }
  }

  componentDidMount(){

    client.topic.publish('/tour_guide', 'std_msgs/String', {'data':"STORY$"+this.state.next_location_id+'$'+this.props.duration})
    var listener = client.topic.subscribe('/tour_guide_data', "std_msgs/String", (message) => {
        message = JSON.parse(message.data)
        console.log(message)

        this.setState({
          labStory: message.story,
          labName: message.name,
          curent_location_id: ''
        })
      });
    
    var listener = client.topic.subscribe('/location', "std_msgs/String", (message) => {

      console.log("Location",message);
        location = parseInt(message.data)
        this.setState({
          curent_location_id: location
        })

        if(this.state.next_location_id == this.state.curent_location_id && this.state.curent_location_id != ''){
            client.topic.publish('/speaker', 'std_msgs/String', {'data':this.state.labStory})  
        }


      });

    client.on("disconnected", function() {
      console.log("Connection disconnected!");
    });
    
  }

  nextPage = () => {
    this.setState({next_location_id: this.state.next_location_id + 1 , curent_location_id: ''});
    client.topic.publish('/tour_guide', 'std_msgs/String', {'data':"STORY$"+this.state.next_location_id+'$'+this.props.duration})
    
  };
  

  render() {
    console.log("Next place",this.state.next_location_id )
    if(this.state.next_location_id == this.state.curent_location_id && this.state.curent_location_id != ''){
      return (
        <View style={styles.container}>
          <Text style={styles.welcome}>
          reached: {this.state.labName}
          </Text>
          <Text style={styles.instructions}>
            Story: {this.state.labStory ? this.state.labStory : "No story for this location"}
          </Text>
          <Button
            onPress={() => {this.nextPage()}}
            title="Go to next location"
            color="#841584"
            accessibilityLabel="Comes to the current location and tells the story"
          />
        </View>
      );
    }

    else if(this.state.curent_location_id == '' || this.state.next_location_id == this.state.curent_location_id){
      return (
        <View style={styles.container}>
          <Text style={styles.instructions}>
            Going to the next place
          </Text>
        </View>
      );
    }

    else if(this.state.curent_location_id != '' || this.state.next_location_id != this.state.curent_location_id){
      return (
        <View style={styles.container}>
          <Text style={styles.instructions}>
            Ooops looks like we went to the wrong locatoion, please take me back to  
            {'\n'}            
            {this.state.labName}
          </Text>
        </View>
      );
    }



  }
  
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});