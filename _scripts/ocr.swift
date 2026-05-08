#!/usr/bin/env swift
import Foundation
import Vision
import AppKit

guard CommandLine.arguments.count >= 2 else {
    FileHandle.standardError.write("usage: ocr.swift <image> [<image>...]\n".data(using: .utf8)!)
    exit(2)
}

for path in CommandLine.arguments.dropFirst() {
    let url = URL(fileURLWithPath: path)
    guard let image = NSImage(contentsOf: url),
          let tiff = image.tiffRepresentation,
          let rep = NSBitmapImageRep(data: tiff),
          let cg = rep.cgImage else {
        FileHandle.standardError.write("could not load \(path)\n".data(using: .utf8)!)
        continue
    }

    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true
    request.recognitionLanguages = ["en-US"]

    // Try each orientation; pick the one with the most recognized characters.
    let orientations: [CGImagePropertyOrientation] = [.up, .right, .down, .left]
    var best: (text: String, score: Int) = ("", 0)

    for orient in orientations {
        let handler = VNImageRequestHandler(cgImage: cg, orientation: orient, options: [:])
        do {
            try handler.perform([request])
            let observations = request.results ?? []
            let text = observations.compactMap { $0.topCandidates(1).first?.string }.joined(separator: "\n")
            if text.count > best.score {
                best = (text, text.count)
            }
        } catch {
            FileHandle.standardError.write("perform failed for \(path) orient=\(orient.rawValue): \(error)\n".data(using: .utf8)!)
        }
    }

    print("===== \(url.lastPathComponent) =====")
    print(best.text)
    print()
}
