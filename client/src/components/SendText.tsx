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
        <div className="flex flex-row items-center bg-rose-100 p-2 rounded">
            <HiOutlineSparkles/>
            <input className="overflow-auto" type="Text" value={textResponse}></input>
            <button onClick={() => state.sendMessage(textResponse, sender)}>
                <BsSend />
            </button>
        </div>
    )
}

export default SendText