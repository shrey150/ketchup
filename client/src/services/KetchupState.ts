import { create } from "zustand"
import { immer } from "zustand/middleware/immer"

export interface Topic {
  id: number
  name: string
  emoji: string
  numMessages: number
  description: string
  summary: string[]
  messages: Message[]
}

export interface Message {
  roomName: string,
  senderName: string,
  text: string,
  timestamp: string
}

export interface KetchupProps {
  topics: Topic[],
}

export const EXAMPLE_PAYLOAD = {
  topics: [
    {
      id: 0,
      name: "Craft2",
      emoji: "👩‍🎨",
      numMessages: 50,
      description: "A cool topic about Craft2",
      summary: [
        "Craft2 is a group of people who like to make things.",
        "We meet every week to make things together.",
        "We make things like art, music, and food.",
        "We also make things like software, hardware, and games.",
      ],
      messages: [
        {
          roomName:"Craft2",
          senderName: "Tyler",
          text:"Yo",
          timestamp:"00:00"
        },
        {
          roomName:"Craft2",
          senderName:"Shrey",
          text:"hi",
          timestamp:"00:11"
        } 
      ]
    },
    {
      id: 1,
      name: "Gamers",
      emoji: "🔥",
      numMessages: 99,
      description: "A cool topic about gamers",
      summary: [
        "Gamers are oppressed.",
        "We fight for gamer rights.",
        "We are gamers.",
        "We are oppressed.",
      ],
      messages: [
        {
          roomName:"Craft2",
          senderName: "Anshu",
          text:"I'm dorkcore !!",
          timestamp:"00:00"
        },
        {
          roomName:"Craft2",
          senderName:"Shrey",
          text:"yep",
          timestamp:"00:12"
        } 
      ]
    },
  ],
}

export const useKetchupState = create(
  immer<KetchupProps>((set, get) => ({
    // topics: [],
    // messages: [],
    ...EXAMPLE_PAYLOAD,
  })),
)


export const EXAMPLE_PAYLOAD_MESSAGE = [
  {
    roomName:"Craft2",
    senderName: "Tyler",
    text:"Yo",
    timestamp:"00:00"
  },
  {
    roomName:"Craft2",
    senderName:"Shrey",
    text:"hi",
    timestamp:"00:11"
  }
]