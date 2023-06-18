import { invoke } from "@tauri-apps/api/tauri"
import type { NextPage } from "next"
import Head from "next/head"
import Image from "next/image"
import { useEffect, useState } from "react"

import TopicCard, { TopicCardProps } from "@/components/TopicCard"
import { useGlobalShortcut } from "@/hooks/tauri/shortcuts"
import { EXAMPLE_PAYLOAD, Topic, useKetchupState } from "@/services/KetchupState"
import { useInterval } from "usehooks-ts"

const Home: NextPage = () => {
  const state = useKetchupState();
  const MSG_THRESHOLD = 1;

  useEffect(() => {
    state.getTopics();
  }, [])

  useInterval(async () => {
    state.fetchUnreadCount();
    if (state.unreadCount > MSG_THRESHOLD && !state.onboarded) {
      state.sendToast('')
    }
  }, 1000)

  return (
    <div className="flex p-8 min-h-screen flex-col bg-white">
      <Head>
        <title>Ketchup</title>
        <meta name="description" content="Ketchup on your messages" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <h1 className="text-center text-3xl mb-11 font-bold">🍅 Ketchup</h1>

      {state.topics.length > 0 ? (
        <div className="grid grid-cols-4 gap-8">
          {state.topics.map(({ id, name, description, messageCount, emoji, summary, textResponse }) => (
            <TopicCard
              id={id}
              key={id}
              name={name}
              description={description}
              messageCount={messageCount}
              emoji={emoji}
              summary={summary}
              textResponse={textResponse}
            />
          ))}
        </div>
      ) : (
        <p className="text-center">Indexing messages...</p>
      )}
    </div>
  )
}

export default Home
