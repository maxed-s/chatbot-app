import './App.css';
import {useEffect, useState} from 'react'
// import postData from './api'

async function postData(url = "", data = {}) { 
    const response = await fetch(url, {
        method: "POST", headers: {
            "Content-Type": "application/json", 
        }, body: JSON.stringify(data),  
    });
    return response.json(); 
}


function App() {
    const [chats, setChats] = useState([]);
    const [que, setQue] = useState("");
    const [asked, setAsked] = useState(false);
    const [count,setCount] = useState(0);

    useEffect(() => {
        console.log("rendering");
    }, [count])

    const ask = async () => {
        if(que === ""){
            alert("empty string not allowed")
            return ;
        }
        setAsked(true);
        const temp = chats;
        const temp1 = {
            question: que,
            answer: null
        }
        temp.push(temp1);
        console.log(temp)
        setChats(temp);
        setQue('');
        const resp = await postData("http://127.0.0.1:5000/api", {"question":que});
        console.log(resp.result)
        temp1.answer = resp.result
        temp.pop()
        temp.push(temp1)
        setChats(temp)
        setCount(count + 1);
    }

    return (
        <div className="App bg-[#343541]">
        <div className="flex h-[100vh] text-white">
            <div className={`left bg-[#202123] w-2/12 `}>

                <button
                    className="w-[90%] py-2 m-2 px-10 space-x-2 border-white border rounded-md flex mx-4 justify-start items-center hover:opacity-70">
                    <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round"
                        stroke-linejoin="round" className="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
                        <line x1="12" y1="5" x2="12" y2="19"></line>
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                    </svg>
                    <span>New Chat</span>
                </button>
                <div className="text-xs m-4 mx-8 text-gray-400">Today</div>
                <div className="chats flex flex-col justify-center items-center space-y-2">


                    <div className="chat space-x-2 opacity-80 w-[90%] px-5 py-2 rounded-md bg-gray-600 cursor-pointer flex justify-start items-center">
                        <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round"
                            stroke-linejoin="round" className="h-4 w-4" height="1em" width="1em"
                            xmlns="http://www.w3.org/2000/svg">
                            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                        </svg>
                        <span>chatQuestion</span>
                    </div>
                    
                </div>

            </div>


            <div className={`right1 w-10/12 flex justify-center items-center flex-col ${!asked ? '' : 'hidden'}`}>
                <div className="text-center w-full text-4xl font-bold my-10">
                    ChatBot
                </div>

                <div className="input w-full text-center my-24 flex items-center justify-center flex-col">
                    <div className="buttonsvg pl-16 w-[50vw] flex">
                        <input className="w-full p-4 bg-gray-600 rounded-md" placeholder="Ask Question" type="text"
                            name="text" id="questionInput" value={que} onChange = {(e) => (setQue(e.target.value))} />

                        <button onClick={ask} id="sendButton" className="relative -left-20 pl-10">
                            <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24"
                                stroke-linecap="round" stroke-linejoin="round" className="h-4 w-4 mr-1" height="1em" width="1em"
                                xmlns="http://www.w3.org/2000/svg">
                                <line x1="22" y1="2" x2="11" y2="13"></line>
                                <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>

            <div className={`right2 w-full flex flex-col items-center h-screen ${asked ? '' : 'hidden'}`}>

            <div className='overflow-y-scroll h-5/6 w-full'>
                {
                chats.map((chat, index) => (
                    <div className='w-full'>
                        <div className="box1 m-auto py-7 flex justify-start w-[40vw] items-center space-x-6">
                            <img className="w-9"
                                src="https://static.vecteezy.com/system/resources/previews/007/409/979/original/people-icon-design-avatar-icon-person-icons-people-icons-are-set-in-trendy-flat-style-user-icon-set-vector.jpg"
                                alt="" />
                            <div id="question">{chat.question}</div>
                        </div>
                        <div className="box2 bg-gray-600 py-7 flex justify-center w-full items-center">
                            <div className="box w-[40vw] flex justify-start space-x-6">
                                <img className="w-9 h-9" src="https://media.licdn.com/dms/image/C4D0BAQGmI6IU2Jrtzw/company-logo_200_200/0/1625160367172?e=2147483647&v=beta&t=xUU5gytiG8gui63hatVCwW7zjfZDufGwfTlLU8-2uak" alt="" />
                                <div className="flex space-y-4 flex-col">
                                    <div id="solution" className={``}>{chat.answer === null ? 'Loading...' : chat.answer}</div>
                                </div>
                            </div>
                        </div>
                    </div>
                ))
                    }
            </div>

                <div className="input h-1/6 w-full text-center flex items-center justify-center flex-col">
                    <div className="buttonsvg pl-16 w-[50vw] flex">
                        <input className="w-full p-4 bg-gray-600 rounded-md" placeholder="Send a Message" type="text"
                            name="text" value={que} onChange = {(e) => (setQue(e.target.value))} />

                        <button onClick={ask} className="relative -left-20 pl-10">
                            <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24"
                                stroke-linecap="round" stroke-linejoin="round" className="h-4 w-4 mr-1" height="1em" width="1em"
                                xmlns="http://www.w3.org/2000/svg">
                                <line x1="22" y1="2" x2="11" y2="13"></line>
                                <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                            </svg>
                        </button>
                    </div>
                </div>

            </div>

        </div>
        </div>
    );
}

export default App;
