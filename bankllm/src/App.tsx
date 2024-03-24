import AppHeader from './components/AppHeader';
import AppFooter from './components/AppFooter';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom"
import CategoryBookListItem from "./components/CategoryBookListItem";
import Chatbot from "./components/Chatbot";


function App() {
  return (
      <Router>
        <AppHeader />
          <Routes>

              <Route path="/" element={<CategoryBookListItem />} />
              <Route path="/categories" element={<CategoryBookListItem />} />
              <Route path="/" element={<CategoryBookListItem />} />
              <Route path="/chatbot" element={<Chatbot />} />
              <Route path="*" element={<div>Page Not Found</div>} />
          </Routes>

        <AppFooter />

      </Router>
  );
}

export default App;

