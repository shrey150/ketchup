type SummaryProps = {
    summary: string[]
}

const Summary = ({ summary }: SummaryProps) => (
    <ul className="list-disc p-4">
        {summary?.map((message, i) => (
          <li key={i}>{message}</li>
        ))}
    </ul>
)

export default Summary