import React from 'react'
import { Message } from '../services/KetchupState'

export type MessageProps = {
    messages: Message[]
}
const MessageList = ({messages}: MessageProps) => {
    return (
        <section id="message">
            <div className="overflow-auto">
                {messages.map((message, index) => (<li key={index}>Group:{message.roomName}[{message.timestamp}],{message.senderName}:"{message.text}"</li>))}
            </div>
        </section>
    );
};

export default MessageList