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
                  src={require('../assets/images/site/butterfly-logo.png')}
                  alt="Prose Bookstore Logo"

              />
          </Link>
          <div id="bookstore-text">
              <h1>
                  <Link to="/" className="text-logo"> Prose Bookstore </Link>
              </h1>
          </div>
      </section>
      <section id="midHeader">
              <form action="">
                  <input type="text" placeholder="Search by Title, Author, or ISBN" className="search-bar"/><br/>
              </form>
              <a id="icon">
                  <img src={require('../assets/images/site/search.png')} width="30px" height="auto"
                       alt="search  icon"/>
              </a>
      </section>
      <section id="rightHeader">
          <div className="header-dropdown" id="categories-button">
              <HeaderDropdown/>
          </div>
          <div>
              <img src={require('../assets/images/site/login.png')} width="30px" height="auto"
                   alt="shopping cart icon"/>
          </div>
          <div id="cartIcon">
              <a href="category.html">
                  <img src={require('../assets/images/site/cart.jpg')} width="30px" height="auto"
                       alt="shopping cart icon"/>
              </a>
              <div id="cartCount">(0)</div>
          </div>
      </section>
  </header>
)
}

export default AppHeader;

