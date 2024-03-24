import AppHeader from './components/AppHeader';
import AppFooter from './components/AppFooter';
import Home from './components/Home'
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom"
import CategoryBookListItem from "./components/CategoryBookListItem";


function App() {
  return (
      <Router>
        <AppHeader />
          <Routes>
              <Route path="/" element={<CategoryBookListItem />} />
              <Route path="/categories" element={<CategoryBookListItem />} />
              <Route path="*" element={<div>Page Not Found</div>} />
          </Routes>

        <AppFooter />

      </Router>
  );
}

export default App;

