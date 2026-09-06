import AudioPlayer from 'react-h5-audio-player'
import 'react-h5-audio-player/lib/styles.css'

function AppAudioPlayer({ src }) {
  return <AudioPlayer src={src} className="themed-audio-player" showJumpControls={false} />
}

export default AppAudioPlayer
