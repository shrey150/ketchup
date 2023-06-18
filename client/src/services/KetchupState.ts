import { create } from "zustand";
import { immer } from "zustand/middleware/immer";
import axios from "axios";

import { isPermissionGranted, requestPermission, sendNotification } from '@tauri-apps/api/notification';

export interface Topic {
  id: number;
  name: string;
  emoji: string;
  messageCount: number;
  description: string;
  summary: string[];
  messages: Message[];
  textResponse: string;
  sender: string;
}

export interface Message {
  groupName: string;
  senderName: string;
  text: string;
  timestamp: string;
  fullName: string;
  pic: string;
}

export interface KetchupProps {
  topics: Topic[];
  unreadCount: number;
  onboarded: boolean;
}

export interface KetchupActions {
  ping: () => void;
  getTopics: () => void;
  sendMessage: (message: string, roomName: string) => Promise<void>;
  fetchUnreadCount: () => Promise<void>;
  fetchStaticData: () => Promise<void>;
  sendToast: (message: string) => Promise<void>;
}

export const EXAMPLE_PAYLOAD = {
  topics: [
    {
      id: 0,
      name: "Craft2",
      emoji: "👩‍🎨",
      messageCount: 50,
      description: "A cool topic about Craft2",
      summary: [
        "Craft2 is a group of people who like to make things.",
        "We meet every week to make things together.",
        "We make things like art, music, and food.",
        "We also make things like software, hardware, and games.",
      ],
      messages: [
        {
          roomName: "Craft2",
          senderName: "Tyler",
          text: "Yo",
          timestamp: "00:00",
        },
        {
          roomName: "Craft2",
          senderName: "Shrey",
          text: "hi",
          timestamp: "00:11",
        },
      ],
    },
    {
      id: 1,
      name: "Gamers",
      emoji: "🔥",
      messageCount: 99,
      description: "A cool topic about gamers",
      summary: [
        "Gamers are oppressed.",
        "We fight for gamer rights.",
        "We are gamers.",
        "We are oppressed.",
      ],
      messages: [
        {
          roomName: "Craft2",
          senderName: "Anshu",
          text: "I'm dorkcore !!",
          timestamp: "00:00",
        },
        {
          roomName: "Craft2",
          senderName: "Shrey",
          text: "yep",
          timestamp: "00:12",
        },
      ],
    },
  ],
};

export const useKetchupState = create(
  immer<KetchupProps & KetchupActions>((set, get) => ({
    topics: [],
    unreadCount: 0,
    onboarded: false, // indicates whether user has opened app after passing unread threshold

    fetchStaticData: async () => {
      try {
        const res = await fetch("http://localhost:8000/api/static");
        const json = await res.json();
        console.log(json);
        set({ topics: json });
      } catch {
        console.log("Error fetching static data");
      }
    },

    ping: async () => {
      try {
        const res = await fetch("http://localhost:8000/ping");
        const json = await res.json();
        console.log(json);
      } catch {
        console.log("Error pinging server");
      }
    },

    fetchUnreadCount: async () => {
      try {
        const res = await fetch("http://localhost:8000/api/unread-count");
        const {unreadCount} = await res.json();
        set({ unreadCount })
      } catch {
        console.log("Error fetching unread counts");
      }
    },

    sendToast: async (message) => {
      let permissionGranted = await isPermissionGranted();
      if (!permissionGranted) {
        const permission = await requestPermission();
        permissionGranted = permission === 'granted';
      }
      if (permissionGranted) {
        sendNotification({
          title: 'Ketchup',
          body: 'It\'s time to get back on track.',
        });
      }
      set({ onboarded: true })
    },

    getTopics: async () => {
      try {
        console.log("Fetching topics");
        // const res = await fetch("http://localhost:8000/api/topics", {
        //   method: "GET",
        //   headers: {
        //     "Content-Type": "application/json",
        //     "Sec-Fetch-Mode": "no-cors",
        //   },
        // }
        // )
        // const topics = await res.json()
        // console.log(topics)
        // set({ topics })

        // rewrite the above request using axios
        const res = await axios.get(
          "http://localhost:8000/api/topics/by-chat",
          {
            timeout: 1000 * 5 * 60,
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        const topics = res.data;
        console.log(topics);
        set({ topics });
      } catch {
        console.log("Error fetching topics");
      }
    },

    sendMessage: async (message: string, roomName: string) => {
      fetch("http://localhost:8000/api/send-message", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message, roomName }),
      });
    },
  }))
);

export const EXAMPLE_PAYLOAD_MESSAGE = [
  {
    roomName: "Craft2",
    senderName: "Tyler",
    text: "Yo",
    timestamp: "00:00",
  },
  {
    roomName: "Craft2",
    senderName: "Shrey",
    text: "hi",
    timestamp: "00:11",
  },
];
