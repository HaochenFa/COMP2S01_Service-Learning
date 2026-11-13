import React from "react";
import { C } from "../theme";
import { Hand } from "./Hand";

/** A photo card holding one hand picture (a training example). */
export const PhotoCard: React.FC<{
  skin: string;
  sleeve: string;
  down?: boolean;
  left?: boolean;
  w?: number;
  style?: React.CSSProperties;
}> = ({ skin, sleeve, down, left, w = 170, style }) => (
  <div
    style={{
      position: "absolute",
      width: w,
      height: w * 1.18,
      background: C.white,
      borderRadius: 22,
      boxShadow: "0 10px 26px rgba(29,36,51,0.16)",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      overflow: "hidden",
      ...style,
    }}
  >
    <Hand skin={skin} sleeve={sleeve} down={down} left={left} size={w * 0.62} />
  </div>
);
