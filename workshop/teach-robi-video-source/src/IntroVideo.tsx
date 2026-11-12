import React from "react";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import {
  DataScene,
  HandsScene,
  OutroScene,
  RulesScene,
  ShowScene,
  TeaseScene,
  TestScene,
  TitleScene,
  TrainScene,
} from "./scenes/Scenes";

export const SCENES = [
  { id: "Title", component: TitleScene, durationInFrames: 150 },
  { id: "Rules", component: RulesScene, durationInFrames: 180 },
  { id: "Hands", component: HandsScene, durationInFrames: 300 },
  { id: "Show", component: ShowScene, durationInFrames: 270 },
  { id: "Train", component: TrainScene, durationInFrames: 180 },
  { id: "Test", component: TestScene, durationInFrames: 270 },
  { id: "Data", component: DataScene, durationInFrames: 150 },
  { id: "Tease", component: TeaseScene, durationInFrames: 240 },
  { id: "Outro", component: OutroScene, durationInFrames: 180 },
] as const;

export const FADE = 12;
export const TOTAL = SCENES.reduce((s, x) => s + x.durationInFrames, 0) - FADE * (SCENES.length - 1);

export const IntroVideo: React.FC = () => (
  <TransitionSeries>
    {SCENES.map((s, i) => {
      const Comp = s.component;
      return (
        <React.Fragment key={s.id}>
          {i > 0 && <TransitionSeries.Transition presentation={fade()} timing={linearTiming({ durationInFrames: FADE })} />}
          <TransitionSeries.Sequence name={s.id} durationInFrames={s.durationInFrames}>
            <Comp />
          </TransitionSeries.Sequence>
        </React.Fragment>
      );
    })}
  </TransitionSeries>
);
