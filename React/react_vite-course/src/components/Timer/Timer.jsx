import { useState, useEffect } from "react"

export default function Timer() {
    const [time, setTime] = useState(10)

    // useEffect(() => {})
    useEffect(function() {
        const interval = setInterval(function() {
            setTime(time - 1)
            console.log(time)
        }, 1000)
        return function() {
            console.log("Cleanup")
            clearInterval(interval)
        }
    })

    return (
        <div>
            Timer: {time}
        </div>
    )
}