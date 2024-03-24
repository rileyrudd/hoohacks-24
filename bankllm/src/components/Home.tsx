
import HomeCategoryList from './HomeCategoryList';
import '../assets/css/global.css';
import '../assets/css/Home.css'



function Home() {
    return (

        <div className="home-page">
            <section id="leftMain">
                <p>Let's find your next 5 star read</p>
                <div>
                    <button className="button">Shop Favorites</button>
                </div>
            </section>
            <section id="rightMain">
                <div id="favorites">
                    <a>
                        <img
                            src={require('../assets/images/books/the-silent-patient.gif')}
                            alt="The Silent Patient book"
                        />
                    </a>
                    <p>"Loved it!"</p>
                </div>
                <div id="favorites">
                    <a>
                        <img
                            src={require('../assets/images/books/none-of-this-is-true.gif')}
                            alt="None of this is True book"
                        />
                    </a>
                    <p>"So relatable"</p>
                </div>
                <div id="favorites">
                    <a>
                        <img
                            src={require('../assets/images/books/the-housemaid.gif')}
                            alt="The Housemaid book"
                        />
                    </a>
                    <p>"So scary!"</p>
                </div>
            </section>
        </div>
    )
}

export default Home;
