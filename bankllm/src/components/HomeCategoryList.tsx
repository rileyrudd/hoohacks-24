import '../assets/css/HomeCategoryList.css';
import {categoryList} from '../types';



function HomeCategoryList(){

    return(

  <ul className ="home-list">
      {categoryList.map((category) => (
          <li className="home-list-li">
              <div className="home-list-div"> {category.name} </div>
          </li>
      ))}


  </ul>

)
}
export default HomeCategoryList;
