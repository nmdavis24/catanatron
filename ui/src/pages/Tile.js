import React from "react";
import cn from "classnames";
import Paper from "@material-ui/core/Paper";

import brickTile from "../assets/tile_brick.svg";
import desertTile from "../assets/tile_desert.svg";
import grainTile from "../assets/tile_wheat.svg";
import lumberTile from "../assets/tile_wood.svg";
import oreTile from "../assets/tile_ore.svg";
import woolTile from "../assets/tile_sheep.svg";
import { SQRT3, tilePixelVector } from "../utils/coordinates";

export function NumberToken({ className, children, style, size }) {
  return (
    <Paper
      elevation={3}
      className={cn("number-token", className)}
      style={{ ...style, width: size * 0.5, height: size * 0.5 }}
    >
      {children}
    </Paper>
  );
}

export default function Tile({ center, coordinate, tile, size }) {
  const w = SQRT3 * size;
  const h = 2 * size;
  const [centerX, centerY] = center;
  const [x, y] = tilePixelVector(coordinate, size, centerX, centerY);

  let contents;
  let resourceTile;
  if (tile.type === "RESOURCE_TILE") {
    contents = <NumberToken size={size}>{tile.number}</NumberToken>;
    resourceTile = {
      BRICK: brickTile,
      SHEEP: woolTile,
      ORE: oreTile,
      WOOD: lumberTile,
      WHEAT: grainTile,
    }[tile.resource];
  } else if (tile.type === "DESERT") {
    resourceTile = desertTile;
  } else if (tile.type === "PORT") {
    let x = 0;
    let y = 0;
    if (tile.direction.includes("SOUTH")) {
      y += size / 3;
    }
    if (tile.direction.includes("NORTH")) {
      y -= size / 3;
    }
    if (tile.direction.includes("WEST")) {
      x -= size / 4;
      if (tile.direction === "WEST") {
        x = -size / 3;
      }
    }
    if (tile.direction.includes("EAST")) {
      x += size / 4;
      if (tile.direction === "EAST") {
        x = size / 3;
      }
    }
    if (tile.resource === null) {
      contents = (
        <div
          className="port"
          style={{
            left: x,
            top: y,
          }}
        >
          3:1
        </div>
      );
    } else {
      contents = (
        <div
          className="port"
          style={{
            left: x,
            top: y,
          }}
        >
          2:1
        </div>
      );
    }
  }

  return (
    <div
      key={coordinate}
      className="tile"
      style={{
        left: x - w / 2,
        top: y - h / 2,
        width: w,
        height: h,
        backgroundImage: `url('${resourceTile}')`,
        backgroundSize: "contain",
      }}
    >
      {contents}
    </div>
  );
}
