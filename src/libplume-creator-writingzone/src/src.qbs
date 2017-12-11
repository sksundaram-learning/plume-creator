import qbs
//import plume-creator-data.qbs as Plume

DynamicLibrary {
    name: "plume-creator-writingzone"
    destinationDirectory: "../../lib"

    cpp.defines: ["PLUME_CREATOR_WRITINGZONE_LIBRARY"]
    cpp.includePaths: [ '.']
    files: ["cursor.cpp",
            "cursor.h",
            "minimap.cpp",
            "minimap.h",
            "plmwritingzone.cpp",
            "plmwritingzone.h",
            "plmwritingzone.ui",
            "richtextedit.cpp",
            "richtextedit.h",
            "sizehandle.cpp",
            "sizehandle.h",
            "toolbar.cpp",
            "toolbar.h",
            "version.info.in"

    ]

    Depends { name: "Qt"; submodules: ["core", "widgets"]}
    Depends { name: "cpp" }
    cpp.optimization: "fast"

    Export {
        Depends { name: "cpp" }
        cpp.includePaths: [product.sourceDirectory]
    }

    Depends { name: "Android.ndk" }
    Android.ndk.appStl: "gnustl_shared"
}
