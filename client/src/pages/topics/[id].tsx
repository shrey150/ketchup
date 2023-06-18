import type { NextPage } from "next"
import { useRouter } from "next/router"
import { EXAMPLE_PAYLOAD, Topic, useKetchupState} from "@/services/KetchupState"
import MessageList from "@/components/MessageList"
import TopicBanner from "@/components/TopicBanner"
import Summary from "@/components/Summary"
import { useMemo, useState } from "react"
import {HiArrowCircleLeft} from "react-icons/hi"


const TopicPage: NextPage = () => {
    
    const router = useRouter()

    const state = useKetchupState();

    
    const topic = useMemo(() => (
        state.topics.find(topic => topic.id === parseInt(router.query.id as string))
    ), [state, router]);
 
    return (
        <div className="max-h-screen">
            <div className="m-10">
                <div className="pb-1">
                    {topic && <TopicBanner
                        id={topic.id}
                        name={topic.name}
                        description={topic.description}
                        messageCount={topic.messageCount}
                        emoji={topic.emoji}
                    />}
                </div>
            
                <div className="grid grid-cols-3 grid-rows-1 gap-1 ">
                    <div className = "rounded drop-shadow-md bg-rose-50 col-span-2">
                        <MessageList messages={topic?.messages ?? []} />
                    </div>
                    <div className = "rounded drop-shadow-md bg-rose-50">
                        {topic && <Summary summary={topic.summary}/>}
                    </div>
                    
                </div>
                <div className="absolute top-0 left-0 p-8">
                    <button onClick={() => router.back()}>
                        <HiArrowCircleLeft size={35} className="animate-bounce"/>
                    </button>
                </div>
            </div>
        </div>
        
    )
}

export default TopicPage