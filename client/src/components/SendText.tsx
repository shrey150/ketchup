import { useKetchupState } from '@/services/KetchupState'
import React from 'react'
import {HiOutlineSparkles} from 'react-icons/hi'
import {BsSend} from 'react-icons/bs'

export type sendTextProp = {
    sender: string
    textResponse: string
}

const SendText = ({textResponse, sender}: sendTextProp) => {

    const state = useKetchupState();

    return (
        <div className="flex flex-row items-center justify-between bg-rose-100 p-2 rounded">
            <HiOutlineSparkles />
            <input className="overflow-auto flex-grow px-4 rounded-lg mx-2" type="Text" value={textResponse}></input>
            <button onClick={(e) => {
                e.stopPropagation();
                state.sendMessage(textResponse, sender)
                alert('Message sent!')
            }}>
                <BsSend />
            </button>
        </div>
    )
}

export default SendText