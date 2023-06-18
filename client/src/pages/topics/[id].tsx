import type { NextPage } from "next"
import { useRouter } from "next/router"

const TopicPage: NextPage = () => {

    const router = useRouter()

    return (
        <div>
            <h1>{router.query.id}</h1>
        </div>
    )
}

export default TopicPage