import React from 'react'
import { Message } from '../services/KetchupState'

export type MessageProps = {
    messages: Message[]
}
const MessageList = ({messages}: MessageProps) => {
    return (
        <div>
            <div className="overflow-scroll p-4 max-h-screen ">
                <h1 className="flex text-3xl justify-left mb-4">Messages:</h1>
                {messages.map((message, index) => (
                    <div className= "flex flex-col bg-rose-200 rounded m-4">
                        <div key={index} className="flex flex-row space-x-3 m-2 justify-between">
                            
                            <div className="flex flex-col text-ellipsis overflow-hidden rounded ">
                                <h1 className="text-2xl font-bold">{message.roomName}</h1>
                                <h2 className="italic">{message.senderName}</h2>
                                <h3 className="">"{message.text}"</h3>
                            </div>
                            <h1 className="self-center items-center">{message.timestamp}</h1>
                        </div>
                    </div>
                    
                ))}

                {/* <table className="table-fixed text-ellipsis overflow-hidden border-collapse w-full">
                    <thead >
                        <tr>
                            <th className="border border-slate-600 bg-rose-200">Time</th>
                            <th className="border border-slate-600 bg-rose-200">Group</th>
                            <th className="border border-slate-600 bg-rose-200">User</th>
                            <th className="border border-slate-600 bg-rose-200 w-3/5">Text</th>
                        </tr>
                    </thead>
                    <tbody>
                        {messages.map((message, index) => (
                            <tr key={index}>
                                <td className="text-center border border-slate-600 bg-rose-100 justify-center">{message.timestamp}</td>
                                <td className=" text-center border border-slate-600 bg-rose-100 justify-center">{message.roomName}</td>
                                <td className=" text-center border border-slate-600 bg-rose-100 justify-center">{message.senderName}</td>
                                <td className="text-center border border-slate-600 bg-rose-100 w-3/5 justify-center">{message.text}</td>
                            </tr>    
                        ))}
                    </tbody>
                </table>
                <div className= "flex flex-col space-y-2">
                    
                </div> */}
            </div>
        </div>
    );
};

export default MessageList