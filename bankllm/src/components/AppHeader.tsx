import HeaderDropdown from './HeaderDropdown';
import '../assets/css/global.css'
import '../assets/css/AppHeader.css';
import { Link } from 'react-router-dom';
function AppHeader(){
    return(

        <header className="container-header">
            <section id="leftHeader">
                <Link className="bookstore-link" to="/" >
                    <img
                        src={require('../assets/images/site/banklogo.png')}
                        alt="Bank Logo"

                    />
                </Link>
            </section>
            <section id="mid">

            </section>
            <section id="rightHeader">
                <Link to="/chatbot">
                    <button className="button categories-button">TalkMoney</button>
                </Link>
                <div className="header-dropdown">
                    <HeaderDropdown/>
                </div>
            </section>
        </header>
    )
}

export default AppHeader;

