import '../assets/css/AppFooter.css'
import '../assets/css/global.css'
import {Link} from "react-router-dom";


function AppFooter(){
return(
  <footer className="container">
    <section className="footer-links">
      <Link className="footer-link" to="/">about</Link>
      <Link className="footer-link" to="/">contact</Link>
      <Link className="footer-link" to="/">directions</Link>
        <Link className="footer-link" to="/">copyright</Link>
    </section>
      <section className="social-media-icons">
          <div className="social-media-link" id="facebook">
              <Link to="/">
                  <img src={require('../assets/images/site/facebook.jpg')} width="40px" height="auto"
                       alt="facebook icon"/>
              </Link>
          </div>
          <div className="social-media-link" id="instagram">
              <Link to="/">
                  <img src={require('../assets/images/site/instagram.png')} width="40px" height="auto"
                       alt="instagram icon"/>
              </Link>
          </div>
      </section>
  </footer>
)
}

export default AppFooter;
