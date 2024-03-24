// Contains all the custom types we want to use for our application
import Classics from './assets/images/categories/classics.jpg';
import Fantasy from './assets/images/categories/fantasy.jpg';
import Mystery from './assets/images/categories/mystery.jpg';
import Romance from './assets/images/categories/romance.jpg';
export interface BookItem {
  bookId: number;
  title: string;
  author: string;
  price: number;
  isPublic: boolean;
  isReadNow: boolean;
}

export interface CategoryItem {
  categoryId: number;
  name: string;
}

export const categoryList = [
  { categoryId: 1001, name: "Profile" },
  { categoryId: 1002, name: "Alerts" },
  { categoryId: 1003, name: "Security" },
  { categoryId: 1004, name: "Support" },

];


export const bookList = [
  {
    bookId: 1005,
    title: "Icebreaker",
    author: "Hannah Grace",
    price: 699,
    isPublic: true,
    isReadNow: false,
  },
  {
    bookId: 1004,
    title: "None of This is True",
    author: "Lisa Jewell",
    price: 1399,
    isPublic: true,
    isReadNow: true,
  },
  {
    bookId: 1002,
    title: "Little Dorrit",
    author: "Charles Dickens",
    price: 599,
    isPublic: true,
    isReadNow: false,

  },
  {
    bookId: 1001,
    title: "All the Light We Cannot See",
    author: "Anthony Doerr",
    price: 699,
    isPublic: true,
    isReadNow: true,

  },
  {
    bookId: 1006,
    title: "The 48 Laws of Power",
    author: "Robert Greene",
    price: 1899,
    isPublic: true,
    isReadNow: false,

  },
  {
    bookId: 1001,
    title: "The Housemaid",
    author: "Freida McFadden",
    price: 12.99,
    isPublic: true,
    isReadNow: true,

  },
  {
    bookId: 1001,
    title: "The Seven Husbands of Evelyn Hugo",
    author: "Taylor Jenkins Reid",
    price: 999,
    isPublic: true,
    isReadNow: false,

  },
  {
    bookId: 1004,
    title: "The Silent Patient",
    author: "Alex Michaelides",
    price: 1299,
    isPublic: true,
    isReadNow: false,
  },
  {
    bookId: 1004,
    title: "Verity",
    author: "Colleen Hoover",
    price: 799,
    isPublic: true,
    isReadNow: true,
  },
];

export const chatbotdata = [
  {
    "id": 1,
    "text": "Hello! How can I help you?",
    "sender": "bot"
  },
  {
    "id": 2,
    "text": "What is your financial goal?",
    "sender": "bot"
  },
  // Add more messages as needed
]
