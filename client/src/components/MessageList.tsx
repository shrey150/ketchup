import React from 'react'
import { Message } from '../services/KetchupState'
import moment from 'moment'
import { BsPersonCircle } from 'react-icons/bs'

export type MessageProps = {
    messages: Message[]
}
const MessageList = ({messages}: MessageProps) => {
    return (
        <div>
            <div className="overflow-scroll p-4">
                <div className="justify-between flex flex-row">
                    <h1 className="text-3xl">Messages:</h1>
                </div>
                {messages[0].groupName && <h1 className="text-2xl justify-left mb-4">Group chat: {messages[0].groupName}</h1>}
                {messages.map((message, index) => (
                    <div className= "flex flex-col bg-rose-200 rounded m-4">
                        <div key={index} className="flex flex-row space-x-3 m-2 justify-between">
                            <div className="flex flex-col text-ellipsis overflow-hidden rounded w-5/6 ">
                                <div className="flex align-center">
                                    {console.log(message.pic)}
                                    {message.pic ? (
                                        <img src={message.pic} height="16" width="16" className="object-cover h-16 w-16 rounded-full mr-4 min-w-16" />
                                    ) : (
                                        <BsPersonCircle className="h-16 w-16 mr-4 min-w-16" />
                                    )}
                                    <div>
                                        <h2 className="italic">{message.fullName ?? message.senderName}</h2>
                                        <h3>"{message.text}"</h3>
                                    </div>
                                </div>
                            </div>
                            <h1 className="self-center items-center">{moment(new Date((parseInt(message.timestamp)/ 1000000) + 978307200000).toString()).fromNow()}</h1>
                        </div>
                    </div>
                    
                ))}
            </div>
        </div>
    );
};

export default MessageList