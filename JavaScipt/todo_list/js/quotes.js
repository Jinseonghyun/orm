const quotes = [
    {
        quote: "The only way to do great work is to love what you do.",
        author: "Steve Jobs",
    },

    {
        quote: "In three words I can sum up everything I've learned about life: it goes on.",
        author: "Robert Frost",
    },

    {
        quote: "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        author: "Nelson Mandela",
    },

    {
        quote: "The future belongs to those who believe in the beauty of their dreams.",
        author: "Eleanor Roosevelt",
    },

    {
        quote: "The only limit to our realization of tomorrow will be our doubts of today.",
        author: "Franklin D. Roosevelt",
    },

    {
        quote: "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        author: "Winston Churchill",
    },

    {
        quote: "Life is what happens when you're busy making other plans.",
        author: "John Lennon",
    },

    {
        quote: "The purpose of our lives is to be happy.",
        author: "Dalai Lama",
    },

    {
        quote: "You miss 100% of the shots you don't take.",
        author: "Wayne Gretzky",
    },

    {
        quote: "The only true wisdom is in knowing you know nothing.",
        author: "Socrates",
    },
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");  
const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;