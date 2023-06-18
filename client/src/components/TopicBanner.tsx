import React from 'react'

export type TopicBannerProps = {
    id: number
    name: string
    description: string
    numMessages: number
    emoji: string
}

const TopicBanner = ({id, name, description, numMessages, emoji}: TopicBannerProps) => {
    return (
        <div className="rounded drop-shadow-md bg-rose-50 p-4">
            <div className="flex flex-row justify-between">
                <div className="flex">
                    <h1 className="text-8xl">{emoji}</h1>
                    <h1 className="text-8xl font-bold">{name}</h1>
                </div>
                <h1 className="self-center text-2xl bg-rose-400 text-white rounded-lg px-2 ml-4 ">{numMessages}</h1>
            </div>
            <h3 className="text-lg italic ">{description}</h3>
        </div>     
    )
}

export default TopicBanner