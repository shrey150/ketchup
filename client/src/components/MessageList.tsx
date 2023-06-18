import React from 'react'
import { Message } from '../services/MessagesState'

export type MessageProps = {
    messages: Message[]
}
const Message = ({messages}: MessageProps) => {
    return (
        <section id="message">
            <div>
                <h1> {messages[0].roomName}</h1>
            </div>
        </section>
    );
};

export default Message