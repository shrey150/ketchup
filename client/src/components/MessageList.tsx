import React from 'react'
import { Message } from '../services/MessagesState'

export type MessageProps = {
    messages: Message[]
}
const MessageList = ({messages}: MessageProps) => {
    return (
        <section id="message">
            <div className="bg-yellow">
                {messages.map((message, index) => (<li key={index}>Group:{message.roomName}[{message.timestamp}],{message.senderName}:"{message.text}"</li>))}
            </div>
        </section>
    );
};

export default MessageList