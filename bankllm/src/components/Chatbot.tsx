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
        url: 'https://29d3-199-111-219-105.ngrok-free.app/advise',
        headers: { }
    };

    const [initialMessages, setInitialMessages] = useState(""); // State to store initial messages


    axios.request(config)
        .then((response) => {
            console.log(JSON.stringify(response.data));
        })
        .catch((error) => {
            console.log(error);
        });

    useEffect(() => {
        // Make API request to fetch initial messages
        axios.get('https://29d3-199-111-219-105.ngrok-free.app/advise')
            .then(response => {
                setInitialMessages(response.data); // Store initial messages in state
            })
            .catch(error => {
                console.error('Error fetching initial messages:', error);
            });
    }, []);



    return(
        <>
            <div className="chat-container">
                <div className="chat-header">
                    TalkMoney
                </div>
                <div className="chat-messages" id="chatMessages">
                    {/*<div className="chat-messages" id="chatMessages">*/}
                    {/*    /!* Render initial messages *!/*/}
                    {/*    {initialMessages && (*/}
                    {/*        <>*/}
                    {/*            <div className="bot-message">{initialMessages['insights']}</div>*/}
                    {/*            <div className="bot-message">{initialMessages['financial health']}</div>*/}
                    {/*            <div className="bot-message">{initialMessages['recommendation']}</div>*/}
                    {/*        </>*/}
                    {/*    )}*/}
                    {/*</div>*/}
                    <div className="chat-messages" id="chatMessages">
                        {/* Render initial messages */}
                        {initialMessages && (
                            <pre className="bot-message">{JSON.stringify(initialMessages, null, 2)}</pre>
                        )}
                    </div>
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

