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
        <div>
            <div className="flex justify-between">
                <div className="flex">
                    <h1 className="text-xl">{emoji}</h1>
                    <h1 className="text-xl">{name}</h1>
                </div>
                <h1 className="text-xl bg-red-600 text-white rounded-lg px-2">{numMessages}</h1>
            </div>
            <h3 className="text-sm">{description}</h3>
        </div>     
    )
}

export default TopicBanner