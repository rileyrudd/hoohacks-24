import HeaderDropdown from './HeaderDropdown';
import '../assets/css/global.css'
import '../assets/css/Chatbot.css'
// import '../assets/css/Chatbot.js'
import '../assets/css/AppHeader.css';
import { Link } from 'react-router-dom';
function Chatbot(){
    return(
        <>
            <div className="chat-container">
                <div className="chat-header">
                    Chat Bot (ChatGPT)
                </div>
                <div className="chat-messages" id="chatMessages">
                </div>
                <div className="input-container">
                    <input type="text" className="input-box" id="userInput" placeholder="Type your Message..."/>
                    <button className="send-button" id="sendMessage">Send</button>
                </div>
            </div>
        </>
    )
}

export default Chatbot;

