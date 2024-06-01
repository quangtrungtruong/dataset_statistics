import ffmpeg
import os
import matplotlib.pyplot as plt


def get_video_duration(video_path):
    probe = ffmpeg.probe(video_path)
    duration = float(probe["format"]["duration"])
    return duration


def main(video_folder):

    durations = []
    for file in os.listdir(video_folder):
        if file.endswith(".mp4"):
            video_path = os.path.join(video_folder, file)
            duration = get_video_duration(video_path)
            durations.append(duration)

    plt.boxplot(durations, vert=False)
    plt.xlabel("Video Duration (s)")
    plt.yticks([])
    plt.grid(axis="x", linestyle="--", linewidth=0.7)
    # Remove the outer border lines
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    plt.subplots_adjust(left=0.1, right=0.9, top=0.3, bottom=0.1)

    vis_path = os.path.join("figures", "video_duration_distribution.png")
    plt.savefig(vis_path, bbox_inches="tight")


if __name__ == "__main__":
    video_folder = "videos"
    main(video_folder)
