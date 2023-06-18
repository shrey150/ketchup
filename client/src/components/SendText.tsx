import React from 'react'
import {HiOutlineSparkles} from 'react-icons/hi'

export type sendTextProp = {
    textResponse: string
}

const SendText = ({textResponse}: sendTextProp) => {
    return (
        <div className="flex flex-row items-center bg-rose-100 p-2 rounded">
            <HiOutlineSparkles/>
            <input type="Text" value={textResponse}></input>

        </div>
    )
}

export default SendText