import { useRouter } from "next/router"
import Summary from "@/components/Summary"

export type TopicCardProps = {
  id: number
  name: string
  description: string
  messageCount: number
  emoji: string
  summary: string[]
}

const TopicCard = ({
  id,
  name,
  description,
  messageCount,
  emoji,
  summary,
}: TopicCardProps) => {

  const router = useRouter()

  const handleClick = () => {
    router.push(`/topics/${id}`)
  }

  return (
    <div className="outline hover:opacity-75 hover:bg-slate-300 p-4 drop-shadow-lg" onClick={handleClick}>
      <div className="flex justify-between">
        <div className="flex pr-2">
          <h1 className="text-xl">{emoji}</h1>
          <h1 className="text-xl ">{name}</h1>
        </div>
        <h1 className=" self-start text-xl bg-red-600 text-white rounded-lg px-2">{messageCount}</h1>
      </div>
      <h3 className="text-sm">{description}</h3>
      <Summary summary={summary} />
    </div>
  );
}

export default TopicCard;