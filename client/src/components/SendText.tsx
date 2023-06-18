import { useKetchupState } from '@/services/KetchupState'
import React, { useState } from 'react'
import {HiOutlineSparkles} from 'react-icons/hi'
import {BsSend} from 'react-icons/bs'

export type sendTextProp = {
    sender: string
    textResponse: string
}

const SendText = ({textResponse, sender}: sendTextProp) => {

    const state = useKetchupState();

    const [userResponse, setUserResponse] = useState(textResponse);
    const handleChange = (e: any) => setUserResponse(e.target.value);

    const handleClick = (e: any) => {
        e.stopPropagation();
        state.sendMessage(textResponse, sender);
        alert('Message sent!');
    }

    return (
        <div className="flex flex-row items-center justify-between bg-rose-100 p-2 rounded">
            <HiOutlineSparkles />
            <input
                className="overflow-auto flex-grow px-4 rounded-lg mx-2"
                type="text"
                value={userResponse}
                onClick={(e) => e.stopPropagation()}
                onChange={handleChange}
            />
            <button onClick={handleClick}>
                <BsSend />
            </button>
        </div>
    )
}

export default SendText