import { useState } from "react";
import axios from "axios";

function OracleChat() {

  const [question, setQuestion] =
    useState("");

  const [answer, setAnswer] =
    useState("");

  const askOracle = async () => {

    try {

      const response =
        await axios.post(

          "http://127.0.0.1:5000/api/chat",

          {
            question
          }
        );

      setAnswer(
        response.data.answer
      );

    }

    catch (err) {

      console.error(err);

    }
  };

  return (

    <div
      style={{
        padding: "20px"
      }}
    >

      <h2>
        Ask ORACLE
      </h2>

      <input

        type="text"

        value={question}

        onChange={(e) =>
          setQuestion(
            e.target.value
          )
        }

        placeholder="
        What AI trends are emerging?
        "

        style={{
          width: "70%",
          padding: "10px"
        }}

      />

      <button

        onClick={askOracle}

        style={{
          marginLeft: "10px",
          padding: "10px"
        }}

      >

        Send

      </button>

      <div
        style={{
          marginTop: "20px",
          border:
            "1px solid #ccc",
          padding: "15px"
        }}
      >

        {answer}

      </div>

    </div>
  );
}

export default OracleChat;