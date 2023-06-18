type SummaryProps = {
    summary: string[]
}

const Summary = ({ summary }: SummaryProps) => {
    return (
        <div className="p-4">
            <h1 className="flex text-3xl justify-left">Summary:</h1>
            <ul className="list-disc p-4 ml-4">
                {summary.map((message, i) => (
                    <li key={i}>{message}</li>
                ))}
            </ul>
        </div>
        
    )
    
}

export default Summary