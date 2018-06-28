import React, { Component } from 'react';
import {
  Platform,
  StyleSheet,
  Text,
  View
} from 'react-native';


import EventEmitter2 from 'eventemitter2'
window.EventEmitter2 = EventEmitter2.EventEmitter2
var RosClient = require("roslibjs-client");
var client = new RosClient({
  url: "ws://192.168.43.137:9090"
});
// client.on("connected", function() {
//   console.log("story chcek");
// });


export default class Story extends React.Component{
  constructor(props) {
    super(props);
    this.state={
      labStory : ''
    }
  }

  componentDidMount(){
    var id;
    id=0;
    //for(i=0;i<9;i++){
     // setTimeout(function(){
    
    //  }, 5000);
    //}

    var labname=["Kcis","LTRC - IRE Lab","LTRC - NLP/ MT Lab","LTRC - Speech Processing Lab","CVIT","ML Lab","DSAC","Cog. Sci"];
    var i = id.toString();
      console.log("Connection established for story");
        client.topic.publish('/tour_guide', 'std_msgs/String', {'data':"LOCATION"})
      var listener = client.topic.subscribe('/tour_guide_data', "std_msgs/String", (message) => {
        console.log(message)
        this.setState({
          labStory: message.data
        })
      });

    client.on("disconnected", function() {
      console.log("Connection disconnected!");
    });
    

    // fetch('http://35ea66c6.ngrok.io/users')
    //   .then((res)=> res.json())
    //   .then(res => this.setState({
    //         labs : res[0],
    //         labName:res[0].name,
    //         labStory:res[0].content
    //       }));
  }


  

  render() {
    return (
      <View style={styles.container}>
        {/* <Text style={styles.welcome}>
         reached: {this.state.labName}
        </Text> */}
        <Text style={styles.instructions}>
          Story: {this.state.labStory}
        </Text>
        
      </View>
    );
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