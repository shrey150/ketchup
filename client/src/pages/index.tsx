import { invoke } from "@tauri-apps/api/tauri"
import type { NextPage } from "next"
import Head from "next/head"
import Image from "next/image"
import { useEffect, useState } from "react"

import TopicCard, { TopicCardProps } from "@/components/TopicCard"
import { useGlobalShortcut } from "@/hooks/tauri/shortcuts"
import { EXAMPLE_PAYLOAD, Topic, useKetchupState } from "@/services/KetchupState"

const Home: NextPage = () => {
  const state = useKetchupState();

  useEffect(() => {
    state.getTopics();
  }, [])

  return (
    <div className="flex p-8 min-h-screen flex-col bg-white">
      <Head>
        <title>Ketchup</title>
        <meta name="description" content="Ketchup on your messages" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <h1 className="text-center text-3xl mb-11 font-bold">🍅 Ketchup</h1>

      <div className="grid grid-cols-4 gap-8">
        {state.topics.map(({ id, name, description, messageCount, emoji, summary }) => (
          <TopicCard
            id={id}
            key={id}
            name={name}
            description={description}
            messageCount={messageCount}
            emoji={emoji}
            summary={summary}
          />
        ))}
      </div>
    </div>
  )
}

export default Home
