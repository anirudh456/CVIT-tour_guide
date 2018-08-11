import React from 'react';
import { ScrollView, TextInput, TouchableHighlight, Image, Alert, Button, StyleSheet, Text, View } from 'react-native';

// import Sound from 'react-native-sound';
import {AudioRecorder, AudioUtils} from 'react-native-audio';

import Location from './Location';
import Welcome from './Welcome';
import Story from './Story';


import EventEmitter2 from 'eventemitter2'
window.EventEmitter2 = EventEmitter2.EventEmitter2
var RosClient = require("roslibjs-client");
var client = new RosClient({
  url: "ws://192.168.43.137:9090"
});
client.on("connected", function() {
  console.log("Connection established!");
  // client.topic.publish('/speaker', 'std_msgs/String', {'data':'welcome to kcis'})
  // var listener = client.topic.subscribe('/speaker', "std_msgs/String", (message) => {
  //   console.log(message)
  // });
});
client.on("disconnected", function() {
  console.log("Connection disconnected!");
});

// For audio recording 
let audioPath = AudioUtils.DocumentDirectoryPath + '/test.aac';

AudioRecorder.prepareRecordingAtPath(audioPath, {
  SampleRate: 44100,
  Channels: 1,
  AudioQuality: "Low",
  AudioEncoding: "aac"
});


function onPressLearnMore() {
  Alert.alert(
    'Sample Alert',
    'Sample Alert',
    [
      {text: 'Ask me later', onPress: () => console.log('Ask me later pressed')},
      {text: 'Cancel', onPress: () => console.log('Cancel Pressed'), style: 'cancel'},
      {text: 'OK', onPress: () => console.log('OK Pressed')},
    ],
    { cancelable: false }
  )
}

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {currentPage: 'Welcome',text:"type to talk to robot", content_duration: ''};
    var ws = new WebSocket('ws://10.42.0.1:9999');

    ws.onopen = () => {
      ws.send('something'); // send a message
    };

    ws.onmessage = (e) => {
      console.log(e.data);
    };
  }


  onSubmitEdit = () => {
    console.log("pressed!");
    client.topic.publish('/user_input', 'std_msgs/String', {'data':this.state.text});
  };


  render() {
    if(this.state.currentPage === 'Home') {
      return (
        <View style={styles.topContainer}>
          <View style={styles.container}>
            <View style={styles.imageContainer}>
              <Image
                source={require('./images/logo.png')}
                style={{width: 130, height: 84}}
              />
            </View>
            <Text style={styles.welcome}>
              Select a time limit on your tour.
              </Text>
            <Button
              onPress={() => {this.setState({currentPage: 'sendMessage' , content_duration: '1'})}}
              title="30 min"
              color="#841584"
              accessibilityLabel="Comes to the current location and then takes the message to specified location"
            />
            <Button
              onPress={() => {this.setState({currentPage: 'sendMessage', content_duration: '2'})}}
              title="45 min"
              color="#841584"
              accessibilityLabel="Comes to the current location and then takes the message to specified location"
            />
            
            <View>
            <TextInput
              style={styles.input}
              textAlign="center"
              onSubmitEditing={this.submitEdit}
              onChangeText={(text) => this.setState({text})}
               />
            <Button
             onPress={this.onSubmitEdit}
              title="submit"
              color="#841584"
            />
          </View>
            
          </View>
        </View>
      );
    }
    else if (this.state.currentPage == 'sendMessage'){
      return (
        <View style={styles.pageHorizontalContainer}>
          <View style={styles.backContainer}>
            <TouchableHighlight onPress={() => {this.setState({currentPage: 'Home'})}}>
              <Image
                source={require('./images/arrow.png')}
                style={{width: 50, height: 50}}
              />
            </TouchableHighlight>
          </View>
          <View style={styles.topPageContainer}>
            <View style={styles.pageContainer}>
              <Story 
              duration={this.state.content_duration}/>
            </View>
          </View>
        </View>
      );
    }
    else if (this.state.currentPage == 'Welcome'){
      return (
        
        <View style={styles.topContainer}>
        <View style={styles.container}>
        <View style={styles.imageContainer}>
              <Image
                source={require('./images/logo.png')}
                style={{width: 130, height: 84}}
              />
            </View>
          <Welcome />
          
          <Button
          onPress={() => {
            client.topic.publish('/speaker', 'std_msgs/String', {'data':'Starting the tour'});
            console.log("Connection ");
            // var listener = client.topic.subscribe('/speaker', "std_msgs/String", (message) => {
            //   console.log(message)
            // });
            this.setState({currentPage: 'Home'})}}
          title="START!"
          color="#841584"
          accessibilityLabel="Comes to the current location and then takes the message to specified location"
        />
  
        </View>
            <View>
            <TextInput
              style={styles.input}
              textAlign="center"
              onSubmitEditing={this.submitEdit}
              onChangeText={(text) => this.setState({text})}
               />
            <Button
             onPress={this.onSubmitEdit}
              title="submit"
              color="#841584"
            />
          </View>
      </View>
      
       
          
      
      );

    }
  }
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#fff',
    height: '70%',
    width: '70%',
    alignItems: 'stretch',
    justifyContent: 'space-around',
  },
  topContainer: {
    backgroundColor: '#fff',
    height: '100%',
    width: '100%',
    alignItems: 'center',
    justifyContent: 'center',
  },
  pageHorizontalContainer: {
    backgroundColor: '#fff',
    height: '100%',
    width: '100%',
    flexDirection: 'row',
    alignItems: 'flex-start',
    justifyContent: 'flex-start',
  },
  topPageContainer: {
    backgroundColor: '#fff',
    height: '100%',
    width: '100%',
    alignItems: 'center',
    justifyContent: 'center',
  },
  pageContainer: {
    backgroundColor: '#fff',
    height: '100%',
    width: '100%',
    alignItems: 'flex-start',
    justifyContent: 'flex-start',
  },
  imageContainer: {
    backgroundColor: '#fff',
    width: '100%',
    alignItems: 'center',
    justifyContent: 'center',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  backContainer: {
    backgroundColor: '#fff',
    height: '15%',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
