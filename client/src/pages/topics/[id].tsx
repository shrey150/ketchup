import type { NextPage } from "next"
import { useRouter } from "next/router"
import { EXAMPLE_PAYLOAD, Topic, useKetchupState} from "@/services/KetchupState"
import MessageList from "@/components/MessageList"
import TopicBanner from "@/components/TopicBanner"
import Summary from "@/components/Summary"
import { useMemo, useState } from "react"


const TopicPage: NextPage = () => {
    
    const router = useRouter()

    const state = useKetchupState();

    
    const topic = useMemo(() => (
        state.topics.find(topic => topic.id === parseInt(router.query.id as string))
    ), [state, router]);
 
    return (
        <div>
            <h1>{router.query.id}</h1>
            {topic && <TopicBanner
                id={topic.id}
                name={topic.name}
                description={topic.description}
                numMessages={topic.numMessages}
                emoji={topic.emoji}
            />}
            <MessageList messages={topic?.messages ?? []} />
            {topic && <Summary summary={topic.summary}/>}
            <button onClick={() => router.back()}>[Back]</button>
        </div>
    )
}

export default TopicPage