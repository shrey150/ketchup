import type { NextPage } from "next"
import { useRouter } from "next/router"
import { EXAMPLE_PAYLOAD_MESSAGE } from "@/services/MessagesState"
import MessageList from "@/components/MessageList"
import { useState } from "react"


const TopicPage: NextPage = () => {
    
    const router = useRouter()
    const [message, setMessage] = useState(EXAMPLE_PAYLOAD_MESSAGE)
    return (
        <div>
            <h1>{router.query.id}</h1>
            <MessageList messages={message} />
        </div>
    )
}

export default TopicPage