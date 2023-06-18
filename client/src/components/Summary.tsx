type SummaryProps = {
    summary: string[]
}

const Summary = ({ summary }: SummaryProps) => {
    return (
        <div className="list-disc">
            <h1 className="flex text-2xl justify-left">Summary</h1>
            <ul className="h-72 overflow-scroll p-1">
                {summary.map((message, i) => (
                    <div className= "flex flex-col bg-rose-200 rounded my-2">
                        <div key={i} className="flex flex-row space-y-2 space-x-3 m-2 overflow-scroll text-ellipsis">
                            <p className= "text-ellipsis"> {message} </p>
                        </div>
                    </div>
                ))}
            </ul>
        </div>
        
    )
    
}

export default Summary