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

function CategoryBookListItem() {
    return (

        <div className="book-lists">
            <li className="book-box">
                <div className="bank-text">
                    <div>Checking ...5637</div>
                    <div>1,765</div>
                </div>
                <button className="button">View Account</button>
            </li>
            <li className="book-box">
                <div className="bank-text">
                    <div>Checking ...2005</div>
                    <div>12,356</div>
                </div>
                <button className="button">View Account</button>
            </li>
            <li className="book-box">
                <div className="bank-text">
                    <div>Checking ...4991</div>
                    <div>19,765</div>
                </div>
                <button className="button">View Account</button>
            </li>
            <li className="book-box">
                <div className="bank-text">
                    <div>Checking ...3012</div>
                    <div>13.62</div>
                </div>
                <button className="button">View Account</button>
            </li>
        </div>


    )
}

export default CategoryBookListItem;