import '../assets/css/AppFooter.css'
import '../assets/css/global.css'
import {Link} from "react-router-dom";


function AppFooter(){
return (
    // <footer className="container">
    //   <section className="footer-links">
    //     <Link className="footer-link" to="/">about</Link>
    //     <Link className="footer-link" to="/">contact</Link>
    //     <Link className="footer-link" to="/">directions</Link>
    //       <Link className="footer-link" to="/">copyright</Link>
    //   </section>
    //     <section className="social-media-icons">
    //         <div className="social-media-link" id="facebook">
    //             <Link to="/">
    //                 <img src={require('../assets/images/site/facebook.jpg')} width="40px" height="auto"
    //                      alt="facebook icon"/>
    //             </Link>
    //         </div>
    //         <div className="social-media-link" id="instagram">
    //             <Link to="/">
    //                 <img src={require('../assets/images/site/instagram.png')} width="40px" height="auto"
    //                      alt="instagram icon"/>
    //             </Link>
    //         </div>
    //     </section>
    // </footer>
    <div>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"></meta>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css"></link>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.min.css"></link>
                <link rel="stylesheet" href="assets/css/style.css"></link>
                    {/*<h2 className="text-center">Super simple page footer*/}
                    {/*    that gives you the basics and lets you customize the rest without getting in the way.*/}
                    {/*</h2>*/}
                    <div className="footer-basic">
                        <footer>
                            <div className="social"><a href="#"><i className="icon ion-social-instagram"></i></a><a href="#"><i className="icon ion-social-snapchat"></i></a><a href="#"><i className="icon ion-social-twitter"></i></a><a href="#"><i className="icon ion-social-facebook"></i></a></div>
                            <ul className="list-inline">
                                <li className="list-inline-item"><a href="#">Home</a></li>
                                <li className="list-inline-item"><a href="#">Services</a></li>
                                <li className="list-inline-item"><a href="#">About</a></li>
                                <li className="list-inline-item"><a href="#">Terms</a></li>
                                <li className="list-inline-item"><a href="#">Privacy Policy</a></li>
                            </ul>
                            <p className="copyright">Company Name © 2023</p>
                        </footer>
                    </div>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/js/bootstrap.bundle.min.js"></script>
    </div>
                    )
}

export default AppFooter;
