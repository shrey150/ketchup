export type TopicCardProps = {
  id: number
  name: string
  description: string
  numMessages: number
  emoji: string
  summary: string[]
}

const TopicCard = ({
  name,
  description,
  numMessages,
  emoji,
  summary,
}: TopicCardProps) => {
  return (
    <div>
      <h1>{name}</h1>
      <h3>{description}</h3>
    </div>
  );
}

export default TopicCard;