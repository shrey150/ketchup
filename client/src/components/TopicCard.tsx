import { useRouter } from "next/router"

export type TopicCardProps = {
  id: number
  name: string
  description: string
  numMessages: number
  emoji: string
  summary: string[]
}

const TopicCard = ({
  id,
  name,
  description,
  numMessages,
  emoji,
  summary,
}: TopicCardProps) => {

  const router = useRouter()

  const handleClick = () => {
    router.push(`/topics/${id}`)
  }

  return (
    <div className="outline hover:opacity-75 hover:bg-slate-300 p-4" onClick={handleClick}>
      <div className="flex justify-between">
        <div className="flex">
          <h1 className="text-xl">{emoji}</h1>
          <h1 className="text-xl">{name}</h1>
        </div>
        <h1 className="text-xl bg-red-600 text-white rounded-lg px-2">{numMessages}</h1>
      </div>
      <h3 className="text-sm">{description}</h3>
      <ul className="list-disc p-4">
        {summary.map((message, index) => (
          <li key={index}>{message}</li>
        ))}
      </ul>
    </div>
  );
}

export default TopicCard;