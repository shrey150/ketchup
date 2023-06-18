import { invoke } from "@tauri-apps/api/tauri"
import type { NextPage } from "next"
import Head from "next/head"
import Image from "next/image"
import { useState } from "react"

import { Card } from "@/components/Card"
import { CardButton } from "@/components/CardButton"
import TopicCard, { TopicCardProps } from "@/components/TopicCard"
import { useGlobalShortcut } from "@/hooks/tauri/shortcuts"
import { EXAMPLE_PAYLOAD, Topic } from "@/services/MessagesState"

const Home: NextPage = () => {
  const [topics, setTopics] = useState<Topic[]>(EXAMPLE_PAYLOAD.topics)

  return (
    <div className="flex p-8 min-h-screen flex-col bg-white">
      <Head>
        <title>Ketchup</title>
        <meta name="description" content="Ketchup on your messages" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <h1 className="text-center text-3xl mb-11">🍅 Ketchup</h1>

      <div className="grid grid-cols-4 gap-8">
        {topics.map(({ id, name, description, numMessages, emoji, summary }) => (
          <TopicCard
            id={id}
            key={id}
            name={name}
            description={description}
            numMessages={numMessages}
            emoji={emoji}
            summary={summary}
          />
        ))}
      </div>
    </div>
  )
}

export default Home
