import { Composition, Folder } from "remotion";
import { IntroVideo, SCENES, TOTAL } from "./IntroVideo";
import { TeachRobi, TEACH_ROBI_FRAMES } from "./v2/TeachRobi";
import { RobiSticker, TMDiagram } from "./v2/Stills";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition id="TeachRobi" component={TeachRobi} width={1920} height={1080} fps={30} durationInFrames={TEACH_ROBI_FRAMES} />
      <Folder name="stills">
        <Composition id="RobiSticker" component={RobiSticker} width={1000} height={1000} fps={30} durationInFrames={1} defaultProps={{ mood: "happy" as const, armL: 16, armR: -16 }} />
        <Composition id="TMDiagram" component={TMDiagram} width={1600} height={900} fps={30} durationInFrames={1} />
      </Folder>
      <Folder name="v1">
        {SCENES.map((s) => (
          <Composition key={s.id} id={s.id} component={s.component} width={1920} height={1080} fps={30} durationInFrames={s.durationInFrames} />
        ))}
        <Composition id="HowComputersLearn" component={IntroVideo} width={1920} height={1080} fps={30} durationInFrames={TOTAL} />
      </Folder>
    </>
  );
};
