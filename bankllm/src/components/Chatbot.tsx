import HeaderDropdown from './HeaderDropdown';
import '../assets/css/global.css'
import '../assets/css/Chatbot.css'
import '../assets/css/AppHeader.css';
import axios from "axios";
import { Link } from 'react-router-dom';
import {useEffect, useState} from "react";
import {chatbotdata} from '../types';
function Chatbot(){

    let config = {
        method: 'get',
        maxBodyLength: Infinity,
        url: 'https://hoohacks24.free.beeceptor.com/advise',
        headers: { }
    };

    axios.request(config)
        .then((response) => {
            console.log(JSON.stringify(response.data));
        })
        .catch((error) => {
            console.log(error);
        });

        // const [messages, setMessages] = useState([]);
        //
        // useEffect(() => {
        //     // Define function to fetch messages from API
        //     const fetchMessages = async () => {
        //         try {
        //             // Make GET request to API endpoint
        //             const response = await axios.get('/api/messages');
        //             // Update state with messages received from the API
        //             setMessages(response.data.messages);
        //         } catch (error) {
        //             console.error('Error fetching messages:', error);
        //         }
        //     };

            // Call fetchMessages function when component mounts
        //     fetchMessages();
        // }, []); // Run only once when component mounts


    return(
        <>
            <div className="chat-container">
                <div className="chat-header">
                    TalkMoney
                </div>
                <div className="chat-messages" id="chatMessages">
                    {/*<div className="chat-messages" id="chatMessages">*/}
                    {/*    {messages.map((message, index) => (*/}
                    {/*        <div key={index} className={message.sender === 'bot' ? 'bot-message' : 'user-message'}>*/}
                    {/*            {message.text}*/}
                    {/*        </div>*/}
                    {/*    ))}*/}
                    {/*</div>*/}
                </div>
                <div className="input-container">
                    <input type="text" className="input-box" id="userInput" placeholder="Let's talk money..."/>
                    <button className="send-button" id="sendMessage">Send</button>
                </div>
            </div>
        </>
    )
}

export default Chatbot;

