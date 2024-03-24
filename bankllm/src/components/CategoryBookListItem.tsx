import '../assets/css/CategoryBookListItem.css';
import '../types'
import "../types";
import {BookItem} from "../types";

const bookImageFileName =  (book:BookItem) => {
  let name = book.title.toLowerCase();
  name = name.replace(/ /g, "-");
  name = name.replace(/'/g, "");
  return `${name}.gif`;
};

function CategoryBookListItem(props:BookItem) {
return (

  <li className="book-box">
   <div className="book-image">
      <img src={require('../assets/images/books/' + bookImageFileName(props))}
        alt="book.title"
      />
    </div>
    <div className="book-title">{props.title }</div>
    <div className="book-author">{ props.author }</div>
    <div className="book-price">${ (props.price / 100).toFixed(2) }</div>
    <button className="button">Add to Cart</button>
      <div id="read-now">      {props.isReadNow && <button className="button" id="read-button">Read Now</button>}
      </div>
  </li>

)
}
export default CategoryBookListItem;
